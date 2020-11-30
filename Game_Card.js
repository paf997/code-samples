/**
* Game_Card: Paolo Fenu, U of S Cmpt 350
* A component used on the game page. Show the main image for a game along with
* other info such as designer, artists, etc
*/

import React from 'react';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import Box from '@material-ui/core/Box';
import Divider from '@material-ui/core/Divider';
import Spinner from '@material-ui/core/CircularProgress';

const useStyles = makeStyles(theme => ({
    root: {
        display: 'flex',
    },
    details: {
        width: 450,
        display: 'flex',
        flexDirection: 'column',
    },
    cover: {
        height:300,
        width: 600,
    },
    description: {
        display: 'flex',
        alignItems: 'center',
        textAlign: 'center',
        paddingLeft: theme.spacing(1),
        paddingBottom: theme.spacing(1),
    },
    button:{
        background:"#4EC5C1",
    },
}));

export default function Game_Card(props) {
    const classes = useStyles();
    const theme = useTheme();

    /* link to external site for rules*/
    const rules =() =>{
        window.open(props.rules);
    }
    
    return (
        <div>
        <Card className={classes.root}>
        {props.img_main ? (<CardMedia
            className={classes.cover}
            image={props.img_main}
            title="img_main"
            /> ) : (<Spinner />)}
        
        <div className={classes.details}>
        <CardContent className={classes.content}>
            <Typography component="h5" variant="h5">
                 {props.title}
            </Typography>
            <Typography variant="subtitle1" color="textSecondary">
                Designer: {props.design}<br />
                Artists: {props.art}<br />
                {props.players} players<br />
                {props.time} Minutes
            </Typography>
            <br /><br />
            <Divider variant="middle" />
            <br />
            <Box justifyContent="center" flexDirection="row" display="flex">
                <Button onClick={rules} variant="contained" color="primary" className={classes.button}> 
                    Download Rules</Button>
            </Box>
        </CardContent>
        
        <div className={classes.description}>
            </div>
                
            </div>
        </Card>
        </div>
    );
}