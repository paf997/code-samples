/**
* NavBar: Paolo Fenu, U of S Cmpt 350
* The navigation bar present in on all pages
*/

import React from 'react'
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import AcUnitRoundedIcon from '@material-ui/icons/AcUnitRounded';
import Die from '@material-ui/icons/Casino';
import { makeStyles } from '@material-ui/core/styles';
import Box from '@material-ui/core/Box';
import Button from "@material-ui/core/Button";
import Menu from './Menu';
import Grid from '@material-ui/core/Grid';

const useStyles = makeStyles(theme => ({
    text: {
        variant: 'h6',
        fontSize:'large',
        fontFamily: 'Montserrat',
        color: 'white',
        textAlign:'left'
    },
    
    text_2: {
        variant: 'h6',
        marginLeft: theme.spacing(1),
        flexGrow: 1,
        fontSize:12,
        fontFamily: 'Montserrat',
        color: 'white',
        textAlign:'center',
        align:'center'
        
    },
    plannerButton: {
        position: 'absolute',
        right: 0,
        marginRight: 15,
        borderRadius: 50,
    },
    left:{
        paddingRight:50,
    },
    
    col:{
        background: "#EC576B"
    }
}));

const NavBar =() => {
    const classes = useStyles();
    return(
        <div>
            <AppBar position='static' className={classes.col}>
                <Toolbar>
                    <Box> 
                        <Die size='medium' onClick={() => {
                            window.location.href ='/';
                        }}>
                            <AcUnitRoundedIcon size='large'/>
                        </Die>
                        </Box>
                            <Box className={classes.left} >
                                <Button  className = {classes.text} onClick={() => {window.location.href ='/'; }}>
                                    BoardGame<br />
                                    SHELFIE
                                </Button>
                        </Box>

                    <Grid container
                        justify="space-between"
                        alignItems="stretch">
                    <Grid item xs={3}>
                        <Button className = {classes.text_2} size={'small'} onClick={() => window.location.href ='/Shelfie'}>
                            Shelfies
                        </Button>
                    </Grid>
                    <Grid item xs={3}>
                        <Menu/>
                    </Grid>
                    <Grid item xs={3}>
                        <Button className = {classes.text_2}  onClick={() => window.location.href ='/Categories'}>
                            Terminology
                        </Button>
                    </Grid>
                    <Grid item xs={3}>
                        <Button className = {classes.text_2} size={'small'} onClick={() => window.location.href ='/Local'}>Local Stores</Button>
                    </Grid>

                </Grid>

                </Toolbar>
            </AppBar>
        </div>
    )
};
export default NavBar;