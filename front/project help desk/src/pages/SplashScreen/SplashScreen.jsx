import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "./SplashScreen.css";

const SplashScreen = () => {
  const [fadeOut, setFadeOut] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const timer = setTimeout(() => {
      setFadeOut(true); // Rozpoczynamy efekt wygaszenia
      setTimeout(() => {
        navigate("/home"); // Nawigujemy do Home po wygaszeniu
      }, 1000); // Czas trwania animacji wygaszenia
    }, 2000); // Czas wyświetlania ekranu Splash

    return () => clearTimeout(timer); // Czyszczenie timera po zakończeniu
  }, [navigate]);

  return (
    <div className={`splash-screen ${fadeOut ? "fade-out" : ""}`}>
      <h1>Witaj w Help Desk</h1>
      <div className="loading-dots">
        <div className="dot"></div>
        <div className="dot"></div>
        <div className="dot"></div>
      </div>
    </div>
  );
};

export default SplashScreen;
