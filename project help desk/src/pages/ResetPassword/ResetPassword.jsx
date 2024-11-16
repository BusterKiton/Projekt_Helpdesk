import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./ResetPassword.css";

const ResetPassword = () => {
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");
  const [isSuccess, setIsSuccess] = useState(false);
  const [countdown, setCountdown] = useState(5); // Dodane odliczanie
  const navigate = useNavigate();

  const handleReset = (e) => {
    e.preventDefault();

    // Dodaj logikę resetowania hasła
    setMessage("Link do resetowania hasła został wysłany na Twój e-mail.");
    setIsSuccess(true);
  };

  useEffect(() => {
    if (isSuccess) {
      const interval = setInterval(() => {
        setCountdown((prev) => {
          if (prev <= 1) {
            clearInterval(interval);
            navigate("/login"); // Przekierowanie na stronę logowania
          }
          return prev - 1;
        });
      }, 1000);

      return () => clearInterval(interval);
    }
  }, [isSuccess, navigate]);

  return (
    <div className="reset-container">
      {isSuccess ? (
        <div className="success-prompt">
          <p className="success-message">{message}</p>
          <p className="redirect-message">
            Przekierowanie na stronę logowania za <span>{countdown}</span>{" "}
            sekund...
          </p>
        </div>
      ) : (
        <div className="reset-box">
          <h2>Przywróć hasło</h2>
          {message && <p className="success-message">{message}</p>}
          <form onSubmit={handleReset}>
            <div className="input-group">
              <label htmlFor="email">Podaj swój e-mail</label>
              <input
                type="email"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>
            <button type="submit" className="reset-button">
              Wyślij link do resetowania
            </button>
          </form>
        </div>
      )}
    </div>
  );
};

export default ResetPassword;
