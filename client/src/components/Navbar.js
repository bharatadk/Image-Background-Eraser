import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Button from '@mui/material/Button';
import  {Link} from 'react-router-dom';
import {Logout} from "./Logout.js"
import scissor from "../assets/scissor.png"
export const NavbarComponent = () =>{

    const navItemStyle = {margin:'10px' , padding:'8px'}

return(

    <>
    <Navbar bg="light" variant="light">
      <Container>
        <Nav className="me-auto">
        <img src={scissor} width="100px" /><span>  </span><h3 style={{color:"blue"}}>     £raser</h3>
            <ul style={{  display: 'flex',   flexDirection: 'row',listStyle:'None' }}>
            <li>                                                                                                                                                                                </li> 
          <li style={navItemStyle}><Link to="#"><Button variant="contained">Home</Button></Link></li>
          <li style={navItemStyle}><Link to="/signup"><Button variant="contained">SignUp</Button></Link></li>
          <li style={navItemStyle}><Link to="/login"><Button variant="contained">Login</Button></Link></li>
          <li style={navItemStyle}><Logout/></li>
          </ul>
        </Nav>
      </Container>
    </Navbar>
  </>
)
}