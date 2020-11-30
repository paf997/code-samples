/**
* Hotness_Card: Paolo Fenu, U of S Cmpt 350
* A component for showing trending boardgames and external links to them 
*/

import React from 'react';
import { makeStyles} from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import CardActionArea from '@material-ui/core/CardActionArea';

const useStyles = makeStyles(theme => ({

    cover: {
        height: 50,
        width: 75,
    },
}));

export default function Hot_Card(props) {
    const classes = useStyles();

    /* Link to external boardgame*/
    const rules =() =>{
        window.open('https://boardgamegeek.com/boardgame/'+props.id);
    }
    
    return (
        <div>
            <Card>
            <CardActionArea onClick={rules}>
            <Box flexDirection="row" display="flex" p={1}>
                <Box flexGrow={1}>
                <CardContent>
                    <Typography variant="subtitle1" color="primary">
                        {props.title}
                    </Typography>
                    <Typography variant="subtitle2" color="textSecondary">
                        Rank: {props.rank}
                    </Typography>
                </CardContent>
                </Box>
                <Box display="flex"alignItems="center">
                    <CardMedia
                    className={classes.cover}
                    image={props.image}
                />
                </Box>
            </Box>
            </CardActionArea>
            </Card>
        </div>
    );
}