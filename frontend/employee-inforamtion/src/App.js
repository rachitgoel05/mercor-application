import React from "react";
import Main from "./components/Main";
import CardDetail from "./components/CardDetail";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";

const App = () => {
	return (
		<BrowserRouter>
			<Routes>
				<Route path="/" element={<Main />} exact />
				<Route path="/employee/:id" element={<CardDetail />} exact />
			</Routes>
		</BrowserRouter>
	);
};

export default App;
