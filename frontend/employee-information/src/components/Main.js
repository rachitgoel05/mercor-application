import React, { useState, useEffect } from "react";
import axios from "axios";
import CardList from "./CardList";
import "./Main.css";
import { CircularProgress, TextField, Typography } from "@mui/material";
import { debounce, throttle } from "lodash";

const Main = () => {
	const [profiles, setProfiles] = useState([]);
	const [searchTerm, setSearchTerm] = useState("");
	const [offset, setOffset] = useState(0);
	const [loading, setLoading] = useState(false);

	const limit = 10; // Number of items to fetch per request

	const fetchProfiles = async () => {
		setLoading(true);
		try {
			const response = await axios.get(
				`https://1456ntefmb.execute-api.ap-south-1.amazonaws.com/Prod/employees?offset=${offset}&limit=${limit}&search=${searchTerm}`
			);
			setProfiles((prevProfiles) => [...prevProfiles, ...response.data]);
			setOffset(offset + 10);
		} catch (error) {
			console.error("Error fetching profiles:", error);
		}
		setLoading(false);
	};

	const debounceOnChange = async (value) => {
		setLoading(true);
		try {
			const response = await axios.get(
				`https://1456ntefmb.execute-api.ap-south-1.amazonaws.com/Prod/employees?search=${value}&limit=${10}`
			);
			setProfiles(response.data);
		} catch (error) {
			console.error("Error fetching search results:", error);
		} finally {
			setLoading(false);
		}
	};
	const handleSearch = debounce((value) => {
		setSearchTerm(value);
		setOffset(0);
		debounceOnChange(value);
	}, 1000);

	const handleScroll = throttle(() => {
		if (
			window.innerHeight + document.documentElement.scrollTop + 500 >
				document.documentElement.offsetHeight &&
			!loading &&
			profiles.length >= limit
		) {
			fetchProfiles();
		}
	}, 500);

	useEffect(() => {
		window.addEventListener("scroll", handleScroll);
		return () => window.removeEventListener("scroll", handleScroll);
	}, [handleScroll]);

	useEffect(() => {
		fetchProfiles();
	}, []);

	return (
		<div className="main">
			<TextField
				label="Search"
				variant="outlined"
				onChange={(e) => handleSearch(e.target.value)}
				placeholder="Search..."
			/>
			{profiles.length > 0 ? (
				profiles.map((profile, index) => (
					<CardList key={profile.id} profile={profile} />
				))
			) : (
				<Typography> {console.log(profiles)} No entries Found</Typography>
			)}
			{loading && (
				<CircularProgress sx={{ display: "block", margin: "16px auto" }} />
			)}
		</div>
	);
};

export default Main;
