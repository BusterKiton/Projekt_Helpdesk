import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Login.css";

const Login = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const handleLogin = (e) => {
    e.preventDefault();

    // Dodaj tutaj logikę walidacji lub integracji z backendem
    if (email.trim() === "" || password.trim() === "") {
      setErrorMessage("Wprowadź poprawne dane logowania.");
      return;
    }

    console.log("Logowanie zakończone sukcesem!");
    navigate("/home"); // Przekierowanie po zalogowaniu
  };

  return (
    <div className="login-container">
      <div className="login-box">
        <h2>Zaloguj się</h2>
        {errorMessage && <p className="error-message">{errorMessage}</p>}
        <form onSubmit={handleLogin}>
          <div className="input-group">
            <label htmlFor="email">E-mail</label>
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className="input-group">
            <label htmlFor="password">Hasło</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="login-button">
            Zaloguj się
          </button>
        </form>
        <div className="login-footer">
          <p className="forgot-password">
            Zapomniałeś hasła?{" "}
            <button
              className="reset-password-link"
              onClick={() => navigate("/reset-password")}
            >
              Przywróć hasło
            </button>
          </p>
          <p className="signup-text">
            Nie masz konta? <a href="/signup">Zarejestruj się</a>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Login;
