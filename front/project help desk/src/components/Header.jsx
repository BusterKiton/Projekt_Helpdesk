import React from "react";
import { useNavigate } from "react-router-dom";
import logo from "../assets/logo.png"; // Import logo
import homeIcon from "../assets/home-icon.png"; // Import ikony "Home"
import submitIcon from "../assets/submit-icon.png"; // Import ikony "Submit Issue"
import profileIcon from "../assets/profile-icon.png"; // Import ikony "Profile"
import logIcon from "../assets/log-icon.png";
import "./Header.css"; // Import stylów CSS

const Header = () => {
  const navigate = useNavigate();

  return (
    <header className="header">
      <img
        src={logo}
        alt="Logo"
        className="logo"
        onClick={() => navigate("/home")}
      />
      <nav className="nav-buttons">
        <button className="icon-button" onClick={() => navigate("/home")}>
          <img src={homeIcon} alt="Home" className="icon icon-home" />
        </button>
        <button
          className="icon-button"
          onClick={() => navigate("/submit-issue")}
        >
          <img
            src={submitIcon}
            alt="Submit Issue"
            className="icon icon-submit"
          />
        </button>
        <button className="icon-button" onClick={() => navigate("/profile")}>
          <img src={profileIcon} alt="Profile" className="icon icon-profile" />
        </button>
        <button className="button icon-button" onClick={() => navigate("/log")}>
          <img src={logIcon} alt="Log" className="icon icon-log" />
        </button>
      </nav>
    </header>
  );
};

export default Header;
