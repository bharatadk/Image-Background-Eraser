import { useNavigate } from "react-router-dom";

export const Logout = () => {
  const navigate = useNavigate();

  return (
    <a href="/" ><button
      onClick={() => {
        sessionStorage.removeItem("ref_token");
        sessionStorage.removeItem("acc_token");
        // navigate("/");
      }}
    >
      ❎
    </button></a>
  );
};
