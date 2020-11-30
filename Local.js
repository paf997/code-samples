/**
* Shelfie Page: Paolo Fenu, U of S Cmpt 350
* A page to show images of other peoples shelfies
*/

import React from 'react';
import './App.css';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Nav from "./components/NavBar";
import Grid from '@material-ui/core/Grid';
import Button from "@material-ui/core/Button";

const useStyles = makeStyles(theme => ({
    
    div:{
        padding:20,
    },
    text : {
        marginLeft: 60,
        marginRight: 60, 
        marginTop: 20,
        fontSize: 20,
        fontFamily: 'Montserrat',
        fontWeight: 900,
        textAlign: 'center',
        color: 'textSecondary'
    }
}));

function Local() {
    const classes = useStyles();
    
    return(
        <div className={classes.div}>
            <Nav/>
                <Typography className = {classes.text} color='textSecondary'>
                        Please support your local suppliers!
                </Typography>
                <Grid container
                    justify="center"
                    alignItems="center">

                <Grid align ={'center'}item xs={12}>
                    <Button className = {classes.text_2}  onClick={() => window.open('https://amazingstoriescomics.com/')}>
                        Amazing Stories
                    </Button>
                </Grid>
                <Grid align ={'center'}item xs={12}>
                    <Button className = {classes.text_2} size={'small'} onClick={() => window.open('https://dragonsdengames.com/')}>
                        Dragons's Den
                    </Button>
                </Grid>
                <Grid align ={'center'}item xs={12}>
                    <Button className = {classes.text_2} size={'small'} onClick={() => window.open('http://8thcomics.com/')}>
                        8th Street Books & Comics
                    </Button>
                </Grid>
            </Grid>
        </div>
    )
}

export default Local;