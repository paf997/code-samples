/**
* GameCar: Paolo Fenu, U of S Cmpt 350
* A component used to create and image carousel for the the game page
*/

import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import GridListTileBar from '@material-ui/core/GridListTileBar';


const useStyles = makeStyles(theme => ({
    root: {
        display: 'flex',
        flexWrap: 'wrap',
        justifyContent: 'space-around',
        overflow: 'hidden',
        backgroundColor: theme.palette.background.paper,
    },
    gridList: {
        flexWrap: 'nowrap',
        // Promote the list into his own layer on Chrome. This cost memory but helps keeping high FPS.
        transform: 'translateZ(0)',
    },
    title: {
        color: theme.palette.primary.light,
    },
        titleBar: {
        background:
      'linear-gradient(to top, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.3) 70%, rgba(0,0,0,0) 100%)',
    },
    }));


export default function GameCar(props) {
    const classes = useStyles();
    
    /* Convert embedded object from props to an array*/
    var imgs = Object.entries(props.imgs);
    var tiles = [];
    imgs.forEach(([key, value]) => {
        tiles.push(value);
    })
    
    return (
        <div className={classes.root}>
            <GridList className={classes.gridList} cols={2.5}>
                {tiles.map((tile,i) => (
            <GridListTile key={i}>
                <img src={tile} alt={tile.title} />
            <GridListTileBar
                title={tile.title}
                classes={{
                    root: classes.titleBar,
                    title: classes.title,
                }}
            />
            </GridListTile>
            ))}
        </GridList>
        <br /><br />
    </div>
  );
}