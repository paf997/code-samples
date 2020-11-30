import React from 'react';
import { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import GridListTileBar from '@material-ui/core/GridListTileBar';
import ListSubheader from '@material-ui/core/ListSubheader';
import IconButton from '@material-ui/core/IconButton';
import InfoIcon from '@material-ui/icons/Info';
const axios = require('axios');
const proxyurl = "https://cors-anywhere.herokuapp.com/";

const useStyles = makeStyles(theme => ({
  root: {
        display: 'flex',
        flexWrap: 'wrap',
        justifyContent: 'space-around',
        overflow: 'hidden',
        backgroundColor: theme.palette.background.paper,
  },
  gridList: {
        width: 800,
        height: 450,
  },
  icon: {
        color: 'rgba(255, 255, 255, 0.54)',
  },
}));

function route_to_id(game_id) {
    console.log(game_id);
    window.location.href="/game_page/id="+game_id;
}

export default function ImgGallery() {
   
    const [data, set_data] = useState({game:[]});

    /* Pull from data base and set state*/ 
    useEffect(() => {
        const fetchData = async () => {
            const result = await axios(
                proxyurl+"https://paolo350-86393.firebaseio.com/Games.json?print=pretty" 
            );
            set_data(result.data);
        };
        fetchData();
    }, []);
    const classes = useStyles();
    
    /* Convert embedded object to an array of objects*/
    var keys = [];
    for(var key in data){
        keys.push(key);
    }
    
    var obj = Object.entries(data);
    var tiles = [];
    obj.forEach(([key, value]) => {
        if(key !== 'Shelfies'){
            tiles.push(value);
        }
    })

    return (
    <div className={classes.root}>
        <GridList cellHeight={180} cols={3} className={classes.gridList}>
        <GridListTile key="Subheader" cols={3} style={{ height: 'auto' }}>
            <ListSubheader component="div"></ListSubheader>
        </GridListTile>
        {tiles.map((tile, i) => (
            <GridListTile key={i}>
                <img src={tile.img_main} 
                    alt="tile img"/>
            <GridListTileBar p={2}
                title={tile.name}
                subtitle={<span>Designed by: {tile.design}</span>}
                actionIcon={
                    <IconButton className={classes.icon} onClick={() => route_to_id(tile.id)}>
                    <InfoIcon />
                    </IconButton>
                    }
                />
            </GridListTile>
            ))}
        </GridList>
    </div>
    );
    }