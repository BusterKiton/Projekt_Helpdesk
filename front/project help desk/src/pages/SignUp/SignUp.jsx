import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios"; // Dodano import axios
import "./SignUp.css";

const Signup = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [showEmployeePrompt, setShowEmployeePrompt] = useState(false);
  const [isEmployee, setIsEmployee] = useState(false);
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [successMessage, setSuccessMessage] = useState("");
  const [countdown, setCountdown] = useState(5);
  const [isRedirecting, setIsRedirecting] = useState(false);

  const validatePassword = (password) => {
    const regex = /^(?=.*[A-Z])(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{12,}$/;
    return regex.test(password);
  };

  const handleEmailChange = (e) => {
    const newEmail = e.target.value;
    setEmail(newEmail);

    const employeeDomains = ["@student.gdansk.merito.pl", "@gdansk.merito.pl"];
    const isEmployeeEmail = employeeDomains.some((domain) =>
      newEmail.endsWith(domain)
    );

    setShowEmployeePrompt(isEmployeeEmail);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (username.trim().length < 3) {
      setErrorMessage("Nazwa użytkownika musi mieć co najmniej 3 znaki.");
      return;
    }

    if (password !== confirmPassword) {
      setErrorMessage("Hasła się nie zgadzają.");
      setPassword("");
      setConfirmPassword("");
      return;
    }

    if (!validatePassword(password)) {
      setErrorMessage(
        "Hasło musi mieć minimum 12 znaków, 1 dużą literę i 1 znak specjalny."
      );
      setPassword("");
      setConfirmPassword("");
      return;
    }

    try {
      const response = await axios.post("http://localhost:8000/api/register/", {
        username,
        email,
        password,
        is_employee: isEmployee,
      });

      if (response.status === 201) {
        setSuccessMessage("Rejestracja zakończona sukcesem!");
        setIsRedirecting(true);
        setTimeout(() => navigate("/login"), 5000); // Przekierowanie po 5 sekundach
      }
    } catch (error) {
      setErrorMessage(
        error.response?.data?.message || "Wystąpił błąd podczas rejestracji."
      );
    }
  };

  useEffect(() => {
    if (isRedirecting) {
      const interval = setInterval(() => {
        setCountdown((prev) => (prev > 1 ? prev - 1 : clearInterval(interval)));
      }, 1000);

      return () => clearInterval(interval);
    }
  }, [isRedirecting]);

  return (
    <div className="signup-container">
      {isRedirecting ? (
        <div className="redirecting-prompt">
          <div className="loading-dots">
            <span></span>
            <span></span>
            <span></span>
          </div>
          <p className="success-message">{successMessage}</p>
          <p className="redirect-message">
            Przekierowanie na stronę logowania za <span>{countdown}</span> sekund...
          </p>
        </div>
      ) : (
        <div className="signup-box">
          <h2>Zarejestruj się</h2>
          {errorMessage && <p className="error-message">{errorMessage}</p>}
          <form onSubmit={handleSubmit}>
            <div className="input-group">
              <label htmlFor="username">Nazwa użytkownika</label>
              <input
                type="text"
                id="username"
                name="username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>
            <div className="input-group">
              <label htmlFor="email">E-mail</label>
              <input
                type="email"
                id="email"
                name="email"
                value={email}
                onChange={handleEmailChange}
                required
              />
            </div>
            {showEmployeePrompt && (
              <div className="employee-prompt">
                <p>
                  Wygląda na to, że jesteś pracownikiem. Czy chcesz
                  zarejestrować się jako pracownik?
                </p>
                <div className="button-group">
                  <button
                    type="button"
                    onClick={() => setIsEmployee(true)}
                    className={isEmployee ? "selected" : ""}
                  >
                    Tak
                  </button>
                  <button
                    type="button"
                    onClick={() => setIsEmployee(false)}
                    className={!isEmployee ? "selected" : ""}
                  >
                    Nie
                  </button>
                </div>
              </div>
            )}
            <div className="input-group">
              <label htmlFor="password">Hasło</label>
              <input
                type="password"
                id="password"
                name="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
            <div className="input-group">
              <label htmlFor="confirm-password">Powtórz hasło</label>
              <input
                type="password"
                id="confirm-password"
                name="confirm-password"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                required
              />
            </div>
            <button type="submit" className="signup-button">
              Zarejestruj
            </button>
          </form>
          <p className="login-text">
            Masz już konto? <a href="/login">Zaloguj się</a>
          </p>
        </div>
      )}
    </div>
  );
};

export default Signup;
