import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";

import { NavbarComponent } from "./components/Navbar.js";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import { Home } from "./components/Home.js";
import { Signup } from "./components/Signup.js";
import { CreateRecipe } from "./components/CreateRecipe";
import { Login } from "./components/Login.js";

// const baseURL = "http://127.0.0.1:5000/recipes/";

// for refreshing token

export const refreshToken = async () => {
  const config = {
    headers: {
      "Content-type": "application/json; charset=UTF-8",
      Authorization: String(sessionStorage.getItem("ref_token")),
    },
  };
  const res = await axios.get(
    "http://127.0.0.1:5000/auth/refresh_token",
    config
  );
  let token = String(res.data.access_token);
  console.log("dsfd", token);
  sessionStorage.setItem("acc_token", token);
  return;
};

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <NavbarComponent />
        <Routes>
          <Route exact path="/" element={<Home />}></Route>
          <Route exact path="/Signup" element={<Signup />}></Route>
          <Route exact path="/Login" element={<Login />}></Route>
          <Route exact path="/CreateRecipe" element={<CreateRecipe />}></Route>
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
