import React from 'react';
import Button from '@material-ui/core/Button';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import { makeStyles } from '@material-ui/core/styles';


const useStyles = makeStyles(theme => ({
    text: {
        variant: 'h6',
        marginLeft: theme.spacing(1),
        flexGrow: 1,
        fontSize:12,
        fontFamily: 'Montserrat',
        color: 'white'
    }
}));

export default function SimpleMenu(props) {
    const classes = useStyles();
    const [anchorEl, setAnchorEl] = React.useState(null);
  
function route_to_id(game_id) {
    console.log(game_id);
    window.location.href="/game_page/id="+game_id;
}
    
const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
    };

const handleClose = (props) => {
    setAnchorEl(null);
    };
    
  return (
      
    <div>
      <Button className={classes.text} aria-controls="simple-menu" aria-haspopup="true" onClick={handleClick}>
        Games
      </Button>
      <Menu
        id="simple-menu"
        anchorEl={anchorEl}
        keepMounted
        open={Boolean(anchorEl)}
        onClose={handleClose}
      >
        <MenuItem onClick={() => route_to_id('Azul')}>Azul</MenuItem>
        <MenuItem onClick={() => route_to_id('Bosk')}>Bosk</MenuItem>
        <MenuItem onClick={() => route_to_id('CatLady')}>Cat Lady</MenuItem>
        <MenuItem onClick={() => route_to_id('Codenames')}>Codenames</MenuItem>
        <MenuItem onClick={() => route_to_id('Everdell')}>Everdell</MenuItem>
        <MenuItem onClick={() => route_to_id('Feudum')}>Feudum</MenuItem>
        <MenuItem onClick={() => route_to_id('MeepleCircus')}>Meeple Circus</MenuItem>
        <MenuItem onClick={() => route_to_id('Root')}>Root</MenuItem>
        <MenuItem onClick={() => route_to_id('Sagrada')}>Sagrada</MenuItem>
        <MenuItem onClick={() => route_to_id('Spirit')}>Spirit Island</MenuItem>
        <MenuItem onClick={() => route_to_id('SpyClub')}>Spy Club</MenuItem>
        <MenuItem onClick={() => route_to_id('Sushi')}>Sushi Go</MenuItem>
        <MenuItem onClick={() => route_to_id('Takenoko')}>Takenoko</MenuItem>
        <MenuItem onClick={() => route_to_id('Ticket')}>Ticket to Ride</MenuItem>
        <MenuItem onClick={() => route_to_id('Wingspan')}>Wingspan</MenuItem>
      </Menu>
    </div>
  );
}