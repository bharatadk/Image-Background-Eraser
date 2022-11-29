import React, { useState } from "react";
import axios from "axios";
import Card from '@mui/material/Card';
import uploader from "../assets/uploader.png"

export const ImageUploadPremium = () => {
  const [userInfo, setuserInfo] = useState({
    file: [],
    filepreview: null,
  });

  const handleInputChange = (event) => {
    setuserInfo({
      ...userInfo,
      file: event.target.files[0],
      filepreview: URL.createObjectURL(event.target.files[0]),
    });
  };

  const [isSucces, setSuccess] = useState(null);

  const submit = async () => {
    const formdata = new FormData();
    formdata.append("avatar", userInfo.file);

    axios
      .post("http://127.0.0.1:5000/upload/premium", formdata, {
        headers: {
           "Content-Type": "multipart/form-data",
           "Authorization": String(sessionStorage.getItem("acc_token")),
      
      },
      })
      .then((res) => {
        // then print response status

        setTimeout(() => {
          setuserInfo({
            ...userInfo,
            file: userInfo.file,
            filepreview: res.data.image_returned,
          });
        }, 1000);
        console.log(res.data.image_returned);
        if (res.data.success === 1) {
          setSuccess("Image upload successfully");
        }
      });
  };

  return (
    <div className="container mr-60">
    <br/>
    <Card sx={{ minWidth: 275,boxShadow: 24 }} style={{borderRadius:"20px",padding:"20px"}}>
    <br/>
    

      <div className="formdesign">
        {isSucces !== null ? <h4> {isSucces} </h4> : null}
        
        <div className="form-row">
        <label for="imageUpload">
          <img src={uploader} width="100%" style={{cursor: "pointer",borderRadius:"30px"}}/>
       </label>
          <input id="imageUpload"
            type="file"
            className="form-control"
            name="upload_file"
            onChange={handleInputChange}
            style={{display:"none"}}
            
          />
           
        </div>
        
       <div style={{display:"flex",flexDirection:"column"}}>

        <div className="form-row" style={{margin:"auto"}}>
            <button
            type="submit"
            style={{background:"Lightgreen",borderRadius:"50%",margin:"5px",padding:"5px"}}
            onClick={() => submit()}
          >
                
          <div>GO</div>      </button>
        </div>
   
      
      
	<div style={{margin:"auto"}}>
      {userInfo.filepreview !== null ? (
        <img
          className="previewimg"
          src={userInfo.filepreview}
          alt="UploadImage"
          height="400"
        />
      ) : null}
      </div>
      </div>
         </div>
      </Card>
    </div>
  );
};
