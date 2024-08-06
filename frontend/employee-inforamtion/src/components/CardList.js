import React from "react";
import { Avatar, Box, Button, Chip, Typography, Paper } from "@mui/material";
import { Link } from "react-router-dom";
import "./CardList.css";

const CardList = ({ profile }) => {
	return (
		<Paper
			elevation={3}
			sx={{
				display: "flex",
				flexDirection: "column",
				padding: "16px",
				borderRadius: "8px",
				width: "50%",
				margin: "10px",
				border: "1px solid #e0e0e0",
			}}
		>
			<Box
				sx={{
					display: "flex",
					alignItems: "center",
					marginBottom: "16px",
					justifyContent: "space-between",
				}}
			>
				<Box
					sx={{ display: "flex", alignItems: "center", marginBottom: "16px" }}
				>
					<Avatar alt={profile.name} sx={{ width: 64, height: 64 }} />
					<Box
						sx={{
							display: "flex",
							flexDirection: "row",
							marginLeft: "16px",
							flex: 1,
						}}
					>
						<Typography variant="h6" sx={{ fontWeight: "bold" }}>
							{profile.name} | Exp:{profile?.experience || "-"} years |{" "}
							{profile?.location?.country}
						</Typography>
					</Box>
				</Box>
				<Box>
					<Link to={`/employee/${profile.userId}`}>
						<Button
							variant="contained"
							sx={{
								backgroundColor: "#f4e9fe",
								color: "#b47ce7",
								borderRadius: "20px",
							}}
						>
							View profile
						</Button>
					</Link>
				</Box>
			</Box>
			<Typography
				variant="body1"
				sx={{ marginBottom: "16px", marginLeft: "10px" }}
			>
				{profile?.summary}
			</Typography>
			<Box
				sx={{
					display: "flex",
					margin: "5px 0",
					justifyContent: "space-between",
				}}
			>
				<h3> Expert in</h3>
				<h3> Commitment</h3>
			</Box>
			<Box
				sx={{ display: "flex", margin: "0", justifyContent: "space-between" }}
			>
				<Box>
					{profile?.skillNames?.map((skill) => (
						<Chip
							key={skill}
							sx={{
								margin: "0 3px",
								backgroundColor: "#f4e9fe",
								color: "#b47ce7",
							}}
							label={skill}
						/>
					))}
				</Box>
				<Box>
					{profile?.fullTimeAvailability != null && <Chip label="Full-Time" />}
					{profile?.partTimeAvailability != null && <Chip label="Part-Time" />}
				</Box>
			</Box>
		</Paper>
	);
};

export default CardList;
