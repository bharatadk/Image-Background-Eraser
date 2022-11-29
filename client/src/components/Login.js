import React, { useState } from "react";
import { Form, Button } from "react-bootstrap";
import { Link } from "react-router-dom";
import { useForm } from "react-hook-form";
// import { login } from '../auth'
import { useNavigate } from "react-router-dom";
import axios from "axios";

export const Login = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm();
  // const access_token =

  const navigate = useNavigate();

  const loginUser = (data) => {
    const requestOptions = {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: data,
    };

    function makePostRequest(path, requestOptionsJSON) {
      axios.post(path, requestOptionsJSON).then(
        (res) => {
          sessionStorage.setItem("acc_token", res.data.access_token);
          sessionStorage.setItem("ref_token", res.data.refresh_token);
          navigate("/");
        },
        (error) => {
          console.log(error);
        }
      );
    }

    makePostRequest("auth/login", requestOptions);

    //    })

    reset();
  };

  return (
    <div className="container">
      <div className="form">
        <h1>Login Page</h1>

        <form>
          {/* Username */}
          <Form.Group>
            <Form.Label>Username</Form.Label>
            <Form.Control
              type="text"
              placeholder="Your username"
              {...register("username", { required: true, maxLength: 25 })}
            />
          </Form.Group>
          {errors.username && (
            <p style={{ color: "red" }}>
              <small>Username is required</small>
            </p>
          )}
          {errors.username?.type === "maxLength" && (
            <p style={{ color: "red" }}>
              <small>Username should be 25 characters</small>
            </p>
          )}
          <br></br>

          {/* Password */}
          <Form.Group>
            <Form.Label>Password</Form.Label>
            <Form.Control
              type="password"
              placeholder="Your password"
              {...register("password", { required: true, minLength: 3 })}
            />
          </Form.Group>
          {errors.username && (
            <p style={{ color: "red" }}>
              <small>Password is required</small>
            </p>
          )}
          {errors.password?.type === "minLength" && (
            <p style={{ color: "red" }}>
              <small>Password should be more than 8 characters</small>
            </p>
          )}
          <br></br>

          {/* Button */}
          <Form.Group>
            <Button
              as="sub"
              variant="primary"
              onClick={handleSubmit(loginUser)}
            >
              Login
            </Button>
          </Form.Group>

          <br></br>
          <Form.Group>
            <small>
              Do not have an account? <Link to="/signup">Create One</Link>
            </small>
          </Form.Group>
        </form>
      </div>
    </div>
  );
};
