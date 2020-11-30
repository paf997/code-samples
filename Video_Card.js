/**
* Vido_Card: Paolo Fenu, U of S Cmpt 350
* A component used for dipslaying video on the Game_Page
*/

import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles({
  root: {
    maxWidth: 350,
  },
  media: {
      height:170,
      display:'flex'
  },
});

export default function MediaCard(props) {
  const classes = useStyles();

    return (
        <Card className={classes.root}>
            <CardMedia
            component="iframe"
            className={classes.media}
      
          image={props.video}
          title="Contemplative Reptile"
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="h2">
            Learn the Rules!
          </Typography>
        </CardContent>
    </Card>
  );
}