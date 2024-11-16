import React from "react";
import { useNavigate } from "react-router-dom";
import "./Home.css";

const Home = () => {
  const navigate = useNavigate();
  return (
    <div className="home">
      <h1>Witamy na stronie Help Desk</h1>
      <p>Aby zgłosić problem, proszę się zalogować</p>
      <button className="login-button" onClick={() => navigate("/login")}>
        Zaloguj
      </button>
    </div>
  );
};

export default Home;
