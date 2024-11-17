import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import ErrorBoundary from "./components/ErrorBoundary";
import Header from "./components/Header";
import SplashScreen from "./pages/SplashScreen/SplashScreen";
import Home from "./pages/Home/Home";
import Login from "./pages/Login/Login";
import SignUp from "./pages/SignUp/SignUp";
import ResetPassword from "./pages/ResetPassword/ResetPassword";
import axios from "axios";

const App = () => {
  const [message, setMessage] = useState(""); // Stan dla komunikatu z backendu

  useEffect(() => {
    // Pobieranie danych z backendu
    axios
      .get("http://localhost:8000/api/hello/")
      .then((response) => {
        setMessage(response.data.message); // Zapisanie odpowiedzi z backendu
      })
      .catch((error) => {
        console.error("Error fetching data from backend:", error);
      });
  }, []);

  return (
    <ErrorBoundary>
      <Router>
        <Header /> {/* Header zawsze widoczny */}
        <Routes>
          <Route path="/" element={<SplashScreen />} />
          <Route path="/home" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/reset-password" element={<ResetPassword />} />
          <Route path="/signup" element={<SignUp />} />
        </Routes>
        {/* Wyświetlanie komunikatu z backendu */}
        <footer style={{ textAlign: "center", marginTop: "20px" }}>
          <p>{message ? `Backend says: ${message}` : "Loading message from backend..."}</p>
        </footer>
      </Router>
    </ErrorBoundary>
  );
};

export default App;
