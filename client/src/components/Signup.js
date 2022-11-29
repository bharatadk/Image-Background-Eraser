import React, { useState } from "react";
import { Form, Button, Alert } from "react-bootstrap";
import { Link } from "react-router-dom";
import { useForm } from "react-hook-form";
import bgImg from "../assets/signup.png";
import axios from "axios";

export const Signup = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm();
  const [show, setShow] = useState(false);
  const [serverResponse, setServerResponse] = useState("");

  const submitForm = (data) => {
    // data.preventDefault();

    if (data.password === data.confirmPassword) {
      const requestOptions = {
        username: data.username,
        email: data.email,
        password: data.password,
      };

      function makePostRequest(path, requestOptions) {
        axios.post(path, requestOptions).then(
          (response) => {
            let result = response.data;
            setServerResponse(result);
            setShow(true);
            console.log(result);
          },
          (error) => {
            console.log(error);
          }
        );
      }

      makePostRequest("auth/signup", requestOptions);

      reset();
    } else {
      alert("Passwords do not match");
    }
  };

  return (
    <div
      className="container"
      style={{ display: "flex", flexDirection: "row" }}
    >
      <div className="form" style={{ width: "40%" }}>
        {show ? (
          <Alert variant="warning">
            This is a {serverResponse.message} alert—check it out!
          </Alert>
        ) : (
          ""
        )}

        <form>
          {/* Username */}
          <Form.Group>
            <Form.Label>Username</Form.Label>
            <Form.Control
              type="text"
              placeholder="Your username"
              {...register("username", { required: true, maxLength: 25 })}
            />

            {errors.username && (
              <small style={{ color: "red" }}>Username is required</small>
            )}
            {errors.username?.type === "maxLength" && (
              <p style={{ color: "red" }}>
                <small>Max characters should be 25 </small>
              </p>
            )}
          </Form.Group>

          {/* Email */}
          <br></br>
          <Form.Group>
            <Form.Label>Email</Form.Label>
            <Form.Control
              type="email"
              placeholder="Your email"
              {...register("email", { required: true, maxLength: 80 })}
            />

            {errors.email && (
              <p style={{ color: "red" }}>
                <small>Email is required</small>
              </p>
            )}

            {errors.email?.type === "maxLength" && (
              <p style={{ color: "red" }}>
                <small>Max characters should be 80</small>
              </p>
            )}
          </Form.Group>

          {/* Password  */}
          <br></br>
          <Form.Group>
            <Form.Label>Password</Form.Label>
            <Form.Control
              type="password"
              placeholder="Your password"
              {...register("password", { required: true, minLength: 8 })}
            />

            {errors.password && (
              <p style={{ color: "red" }}>
                <small>Password is required</small>
              </p>
            )}
            {errors.password?.type === "minLength" && (
              <p style={{ color: "red" }}>
                <small>Min characters should be 8</small>
              </p>
            )}
          </Form.Group>

          {/* confirmPassword */}
          <br></br>
          <Form.Group>
            <Form.Label>Confirm Password</Form.Label>
            <Form.Control
              type="password"
              placeholder="Your password"
              {...register("confirmPassword", { required: true, minLength: 8 })}
            />
            {errors.confirmPassword && (
              <p style={{ color: "red" }}>
                <small>Confirm Password is required</small>
              </p>
            )}
            {errors.confirmPassword?.type === "minLength" && (
              <p style={{ color: "red" }}>
                <small>Min characters should be 8</small>
              </p>
            )}
          </Form.Group>

          {/* SubmitButton */}
          <br></br>
          <Form.Group>
            <Button
              as="sub"
              variant="primary"
              onClick={handleSubmit(submitForm)}
            >
              SignUp
            </Button>
          </Form.Group>

          <br></br>
          <Form.Group>
            <small>
              Already have an account, <Link to="/login">Log In</Link>
            </small>
          </Form.Group>
          <br></br>
        </form>
      </div>
      <div className="col-2">
        <img src={bgImg} alt="" />
      </div>
    </div>
  );
};
