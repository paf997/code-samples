/**
* Game_Page: Paolo Fenu, U of S Cmpt 350
* A page template for each game that is featured
*/

import React, { useState, useEffect } from 'react';
import './App.css';
import { makeStyles } from '@material-ui/core/styles';
import Nav from "./components/NavBar";
import Box from '@material-ui/core/Box';
import Paper from '@material-ui/core/Paper';
import GameCard from "./components/Game_Card";
import VideoCard from "./components/Video_Card";
import Imgs from "./components/GameCar";
import {useParams} from 'react-router-dom';
import Spinner from '@material-ui/core/CircularProgress';
const axios = require('axios');
const proxyurl = "https://cors-anywhere.herokuapp.com/";

const useStyles = makeStyles(theme => ({

    paper: {
        backgroundColor:"#E5E338",
        width:"80%",
    },
    div:{
        flexGrow: 1
    }
}));

function Game_Page() {
    
    let { id } = useParams();

    const [data, set_data]= useState([]);
    const [imgs, set_imgs] = useState([]);
    /* Pull from data base and set state*/ 
    useEffect(() => {
        const fetchData = async () => {
            const result = await axios(
                proxyurl+"https://paolo350-86393.firebaseio.com/Games/"+id+".json"
            );
            set_data(result.data);
            set_imgs(result.data.imgs);
        };
        fetchData();
    }, []);

    const classes = useStyles();
    
    return(
        <div className={classes.div}>
            <Nav/>
        <Box display="flex" m = {1} justifyContent='center'>
            {data ? (<GameCard
                title = {data.name}
                players = {data.players}
                art = {data.art}
                design = {data.design}
                description = {data.description}
                img_main = {data.img_main}
                rules={data.rules}
                time={data.time}
            />) : (<Spinner />)}
        </Box>
        
        <Box align='center'>
        <Paper className={classes.paper}>                   
            {data.descript} 
        </Paper>  
        </Box>
        <Box justifyContent="center" flexDirection="row" display="flex" >
            <Box m = {3}>
                <VideoCard
                    video={data.video}
                />
            </Box>
            <Box m = {3}>
                <VideoCard
                    video={data.video_2}
                />
            </Box>
        </Box>
        
        <Imgs
            imgs={imgs}
        />
        </div>
    )
}

export default Game_Page;