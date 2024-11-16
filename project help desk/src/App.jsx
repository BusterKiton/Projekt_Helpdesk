import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import ErrorBoundary from "./components/ErrorBoundary";
import Header from "./components/Header";
import SplashScreen from "./pages/SplashScreen/SplashScreen";
import Home from "./pages/Home/Home";
import Login from "./pages/Login/Login";
import SignUp from "./pages/SignUp/SignUp";
import ResetPassword from "./pages/ResetPassword/ResetPassword";

const App = () => {
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
      </Router>
    </ErrorBoundary>
  );
};

export default App;
