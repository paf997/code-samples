/**
* Shelfie Page: Paolo Fenu, U of S Cmpt 350
* A page to show images of other peoples shelfies
*/

import React, { useState, useEffect } from 'react';
import './App.css';
import { makeStyles } from '@material-ui/core/styles';
import Nav from "./components/NavBar";
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import CatCard from "./components/Category_Card";
const axios = require('axios');
const proxyurl = "https://cors-anywhere.herokuapp.com/";

const useStyles = makeStyles(theme => ({
    
    div:{
        padding:20,
    },  
    div_gallery:{
        padding: 60,
    },

    gridList: {
        width: 800,
        height: 550,
    },  
}));

function Shelfie() {
    
    const [data, set_data]= useState([]);
    const classes = useStyles();
    
    /* Pull from data base and set state*/ 
    useEffect(() => {
        const fetchData = async () => {
            const result = await axios(
                proxyurl+"https://paolo350-86393.firebaseio.com/Games/Shelfies.json" 
            );
            set_data(result.data);
        };
        fetchData();
    }, []);
    
    var filtered = data.filter(function (item) {
        return item != null;
    });
    
    return(
        <div className={classes.div}>
            <Nav/>
            <div className={classes.div_gallery} align={'center'}>
                <CatCard 
                category={"Shelfie"}
                descript={"A photo taken to show off what is on someone's shelf. SHELFIES are usually taken to show off books, figures, or collectable memorabilia IN ALL IT'S GLORY! Many believe the term was coined by author Rick Riordan."}
            />
            <br />
                <div>
                    <GridList cellHeight={260} className={classes.gridList} cols={4}>
                        {filtered.map((tile,i) => (
                        <GridListTile key={i} cols={1}>
                        <img src={tile}  
                            alt="tile img"/>
                        </GridListTile>
                        ))}
                    </GridList>
                </div>
            </div>
        </div>
    )
}

export default Shelfie;