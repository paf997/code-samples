/**
* Category_Card: Paolo Fenu, U of S Cmpt 350
* A page for terminaolgy and game categories
*/
import React from 'react';
import './App.css';
import { makeStyles } from '@material-ui/core/styles';
import Nav from "./components/NavBar";
import CatCard from "./components/Category_Card";

const useStyles = makeStyles(theme => ({
    div:{
        padding: 5,
    }
}));

function Game_Page() {
    
    const classes = useStyles();
    
    return(
        <div className={classes.div}>
            <Nav/><br />
            <CatCard 
                descript ={"An abstract strategy game is a strategy game in which the theme is not   important to the experience of playing. Many of the world's classic board games, including chess, Go, checkers and draughts, xiangqi (Chinese chess), shogi (Japanese chess), Reversi (marketed as \"Othello\"), nine men's morris, and most mancala variants, fit into this category."}
                category={"Abstract"}  
            />
            <CatCard 
                category={"EuroGame"}
                descript={"A Eurogame, also called a German-style board game, German game, or Euro-style game, is a class of tabletop games that generally has indirect player interaction and abstract physical components.Eurogames are sometimes contrasted with American-style board games, which generally involve more luck, conflict, and drama.Eurogames are usually less abstract than chess or Go, but more abstract than wargames. Likewise, they generally require more thought and planning than party games such as Pictionary or Trivial Pursuit."}
            />
            <CatCard 
                category={"Co-operative"}
                descript={"Cooperative board games are board games in which players work together to achieve a common goal, the result being either winning or losing as a group. As the name suggests, cooperative games stress cooperation over competition. This type of board game attracts people who enjoy the social aspect of games and is a good way to get new board game players interested in the hobby. Either the players win the game by reaching a pre-determined objective, or all players lose the game, often by not reaching the objective before a certain event ends the game."}
            />
        
            <CatCard 
                category={"Dexterity/Action"}   
                descript={"Action/Dexterity games often compete players' physical reflexes and co-ordination as a determinant of overall success."}
            />
            <CatCard 
                category={"Shelfie"}
                descript={"A photo taken to show off what is on someone's shelf. SHELFIES are usually taken to show off books, figures, or collectable memorabilia IN ALL IT'S GLORY! "}
            />
            <CatCard 
                category={"Kallax"}
                descript={"Square shelving unit by IKEA very popular among gamers.It can be placed vertically or horizontally, stacked, set side by side, and their square shelves can be personalized with inserts, doors, boxes, baskets and various accessories, making it very adaptable. But mostly it suits board games especially well, the standard square boxes or the coffin box, and will hold the tiny card game as well as the gigantic Kickstarter edition. And without the all-too-common problems of sagging, bulging, sliding, or dishing."}
            />
            <CatCard 
                category={"Meeple"}
                descript={"A small person-shaped figure used as a player's token in a board game."}
            />
            <CatCard 
                category={"Analysis Paralysis(AP)"}
                descript={"Games provide a microcosm for decision-making where there can be adversaries, hidden or missing information, random events, complex options, and consequences. In this context, analysis paralysis denotes a state where a player is so overwhelmed by aspects of the decision tree that he or she faces that the player's turn takes an inordinate amount of time."}
            />
        
        </div>
    )
}

export default Game_Page;