import axios from "axios";
import { useState } from "react";
import { refreshToken } from "../App.js";
import { ImageUpload } from "./ImageUpload.js";
import { ImageUploadPremium } from "./ImageUploadPremium.js";
import wall from "../assets/wall.png"
export const Home = () => {
  const [proData, setproData] = useState("");

  const fetchQuotes = async () => {
    const config = {
      headers: {
        "Content-type": "application/json; charset=UTF-8",
        "Authorization": String(sessionStorage.getItem("acc_token")),
      },
    };
    const res = await axios.get("http://127.0.0.1:5000/auth/protected", config);
    setproData(res.data.message);
    if (res.data.message === "JWT-expired") {
      console.log(res.data.message);
      refreshToken();
    }
    return;
  };

  fetchQuotes();

  return (
    <div className="home">
      {proData &&
      proData !== "" &&
      proData !== "invalid-JWT" &&
      proData !== "JWT-expired" ? (
       <div className="container" style={{display:"flex",flexDirection:"row"}}>
        <div className="container">
          <br></br><br></br> <br></br> <br></br>

          <img src={wall} width="500px"/>
          <h2 style={{ color: "#FFD700" }}>    Remove Image Background</h2>
          <h4 >            100% Automatically and 🆓</h4>

        </div>
        <div className="container">
                  <ImageUploadPremium />

        </div>
        </div>
      ) : (
        <div className="container" key={proData}>
          {/* {proData} */}
          <br></br>
          <h1> Please login for High-Quality Images</h1>
          <br></br>
          <ImageUpload />
        </div>
      )}
    </div>
  );
};
