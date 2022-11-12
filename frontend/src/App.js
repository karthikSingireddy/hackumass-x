import * as React from 'react';
import DiningHall from './DiningHall';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
// import MenuIcon from '@mui/icons-material/Menu';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
// import AdbIcon from '@mui/icons-material/Adb';

const pages = ['worcester', 'frank', 'hamp', 'berk'];
const settings = ['Profile', 'Account', 'Dashboard', 'Logout'];

function App() {
  const [anchorElNav, setAnchorElNav] = React.useState("worcester");
  const [anchorElUser, setAnchorElUser] = React.useState(null);
  const [diningHall, setDiningHall] = React.useState('worcester');

  // const handleOpenNavMenu = () => {
  //   setAnchorElNav(Event.currentTarget);
  // };
  // const handleOpenUserMenu = () => {
  //   setAnchorElUser(Event.currentTarget);
  // };

  const handleCloseNavMenu = () => {
    console.log("clicked this");
    setAnchorElNav(null);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

  return (
    <>
      <AppBar position="static">
        <Container maxWidth="xl">
          <Toolbar disableGutters>
            <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
              {pages.map((page) => (
                <Button
                  key={page}
                  onClick={() => {setDiningHall(page); console.log("state is " + page)}}
                  sx={{ my: 2, color: 'white', display: 'block' }}
                >
                  {page}
                </Button>
              ))}
            </Box>
          </Toolbar>
        </Container>
      </AppBar>
      <DiningHall name={diningHall}></DiningHall>
    </>
  );
}
export default App;
