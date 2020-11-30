/**
* Category_Card: Paolo Fenu, U of S Cmpt 350
* A Card component used for the Terminolgy and Category page
*/

import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Divider from '@material-ui/core/Divider';
import Typography from "@material-ui/core/Typography";
import Card from '@material-ui/core/Card';

const useStyles = makeStyles(theme => ({

    paper: {
        border: 'solid',
        borderWidth: '5px',
        borderColor:"#E5E338",
        padding: 5, 
    },
    div:{
        padding: 5,
    }
    
}));

function Category_Card(props) {
    
    const classes = useStyles();
    
    return(
        <div className={classes.div}>
            <Card>
            <Paper className ={classes.paper}>
                <Typography variant="h5" component="h2">
                    {props.category}
                </Typography>
                <Divider/>
                <Typography variant="body2" color="textSecondary" component="p">
                    {props.descript}
                </Typography>
            </Paper>
            </Card>
        </div>
    )
}

export default Category_Card;