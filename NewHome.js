/**
* NewHome: Paolo Fenu, U of S Cmpt 350
* Web site's home page
*/

import React, { useState, useEffect } from 'react';
import './App.css';
import { makeStyles } from '@material-ui/core/styles';
import Nav from "./components/NavBar";
import HotCard from "./components/Hotness_Card";
import Gallery from './components/ImgGallery';
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';
const axios = require('axios');
const proxyurl = "https://cors-anywhere.herokuapp.com/"; // used to prevent CORS error

const useStyles = makeStyles(theme => ({
    text : {
        marginLeft: 60,
        marginRight: 60, 
        marginTop: 20,
        fontSize: 20,
        fontFamily: 'Montserrat',
        fontWeight: 900,
        textAlign: 'center',
        color: 'textSecondary'
    },
    div: {
        border: 'solid',
        borderWidth: '1px',
        borderColor:"#E5E338",
        padding: 5, 
        width:300
    },
    pop:{
        fontSize: 20,
        fontFamily: 'Montserrat',
        fontWeight: 900,
        textAlign: 'center',
    },
    descript:{
        paddingLeft:50,
        paddingRight:50,
    }
}));


function NewHome() {
    
    const [data, set_data]= useState([]);
    
    /* Pull from data base and set state*/ 
    useEffect(() => {
        const fetchData = async () => {
            const result = await axios(
                proxyurl+"	https://bgg-json.azurewebsites.net/hot" 
            );
            set_data(result.data);
        };
        fetchData();
    }, []);

    const classes = useStyles();
    
    return(
        <div style={{ width: '100%' }}>
            <Nav/>
            <Box className={classes.descript}> 
                <Typography className = {classes.text} color='textSecondary'>
                        Welcome to BoardGame SHLEFIE!
                </Typography>
                <Typography color="textSecondary" align={'center'}>
                    A site for boardgame enthusiasts or those looking for looking a new game. Checkout my collection below or see what is trending as on board game geek.
                </Typography>
            </Box>
            <Box display="flex" m = {4}>
                <Box m = {2}>  <Gallery/> </Box>
                    <Box style={{ width: 200 }} display="flex"p={2}> 
                        <div className={classes.div}> 
                            <Typography className = {classes.pop}>
                                Popular trending games
                            </Typography>
                                {data.slice(0,4).map((tile,i) => (
                                <HotCard key={i}
                                image = {tile.thumbnail} 
                                title={tile.name}
                                rank={tile.rank}
                                id={tile.gameId}
                            />
                        ))} 
                    </div>
                </Box>
            </Box>  
        </div>
    )
}

export default NewHome;