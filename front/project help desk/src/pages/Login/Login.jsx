import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "./Login.css";

const Login = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");  // Zmieniono email na username
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();

    if (username.trim() === "" || password.trim() === "") {
      setErrorMessage("Wprowadź poprawne dane logowania.");
      return;
    }

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/login/", {
        username: username,
        password: password,
      });

      if (response.status === 200) {
        const data = response.data;
        console.log("Logowanie zakończone sukcesem!");
        console.log("Token: ", data.token);
        localStorage.setItem("token", data.token);
        navigate("/home");
      } else {
        setErrorMessage("Nieprawidłowe dane logowania.");
      }
    } catch (error) {
      if (error.response && error.response.data) {
        setErrorMessage(error.response.data.message);
      } else {
        setErrorMessage("Wystąpił błąd podczas logowania. Spróbuj ponownie.");
      }
    }
  };

  return (
    <div className="login-container">
      <div className="login-box">
        <h2>Zaloguj się</h2>
        {errorMessage && <p className="error-message">{errorMessage}</p>}
        <form onSubmit={handleLogin}>
          <div className="input-group">
            <label htmlFor="username">Nazwa użytkownika</label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
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
