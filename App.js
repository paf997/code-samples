import React from 'react';
import './App.css';
import NewHome from "./NewHome";
import Game_Page from "./Game_Page";
import Categories from "./Categories";
import Shelfie from "./Shelfie";
import Local from "./Local";
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';

export default function App() {

  return (
    <div>
        <Router>
            <Switch>
                <Route exact path="/">
                    <NewHome/>
                </Route>
                <Route path="/game_page/id=:id">
                    <Game_Page/>
                </Route>
                <Route path="/Categories">
                    <Categories/>
                </Route>
                <Route path="/Shelfie">
                    <Shelfie/>
                </Route>
                <Route path="/Local">
                    <Local/>
                </Route>
            </Switch>
        </Router>
    </div>
  );
}
