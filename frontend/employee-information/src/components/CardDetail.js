import React, { useEffect, useState, useRef } from "react";
import { useParams, useNavigate } from "react-router-dom";

import "./CardDetail.css";
import {
	Card,
	CardContent,
	Typography,
	Avatar,
	Button,
	Chip,
	Box,
	Grid,
	IconButton,
	List,
	ListItem,
	ListItemAvatar,
	ListItemText,
	Divider,
} from "@mui/material";
import EmailIcon from "@mui/icons-material/Email";
import BookmarkIcon from "@mui/icons-material/Bookmark";
import ShareIcon from "@mui/icons-material/Share";
import CloseIcon from "@mui/icons-material/Close";
import ArrowForwardOutlinedIcon from "@mui/icons-material/ArrowForwardOutlined";
import axios from "axios";

const CardDetail = () => {
	const awardsData = [
		"Google Cloud Program certified",
		"Qualified for Smart India Hackathon at College Level",
		"Secured global rank-54 out of 10k students in Job-a-thon (GeeksForGeeks)",
		"350+ questions on Leetcode, 4 * in Problem Solving at Hackerrank",
		"Zonal Level Winner at multiple Chess Competition",
	];
	const { id } = useParams();
	const [employeeDetailState, setEmployeeDetailData] = useState();
	const fetchIndividual = async () => {
		try {
			const employeeDetailData = await axios.get(
				`http://localhost:3001/employees/${id}`
			);
			setEmployeeDetailData(employeeDetailData.data);
		} catch (error) {
			console.error("Error fetching profiles:", error);
		}
	};
	useEffect(() => {
		fetchIndividual();
	}, []);
	useEffect(() => {
		if (interviewRef.current) {
			interviewRef.current.scrollIntoView({
				behavior: "smooth",
				block: "start",
			});
		}
	}, [employeeDetailState]);
	const navigate = useNavigate();

	const handleClose = () => {
		navigate("/");
	};
	// Create refs for each section
	const interviewRef = useRef(null);
	const experienceRef = useRef(null);
	const educationRef = useRef(null);
	const awardsRef = useRef(null);
	const projectsRef = useRef(null); // Add this when you have the project section
	const handleScrollTo = (ref) => {
		ref.current.scrollIntoView({ behavior: "smooth", block: "start" });
	};
	return (
		<div style={{ backgroundColor: "white" }}>
			<Box
				sx={{
					display: "flex",
					alignItems: "center",
					justifyContent: "center",
					minHeight: "100vh",
					position: "relative",
					backgroundColor: "#f5f5f5",
					padding: 2,
				}}
				ref={interviewRef}
			>
				<Card
					sx={{
						width: "900px",
						borderRadius: "10px",
						boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.1)",
					}}
				>
					<CardContent>
						<IconButton
							onClick={handleClose}
							sx={{ position: "absolute", top: 10, right: 10 }}
						>
							<CloseIcon />
						</IconButton>
						<Grid container spacing={2} alignItems="center">
							<Grid item>
								<Avatar alt="Profile Picture" sx={{ width: 56, height: 56 }} />
							</Grid>
							<Grid item xs>
								<Typography variant="h6" component="div">
									{employeeDetailState?.name} | Exp:{" "}
									{employeeDetailState?.experience} years |{" "}
									{employeeDetailState?.location?.country}
								</Typography>
							</Grid>
						</Grid>
						<Box sx={{ mt: 2 }}>
							<Button
								variant="contained"
								startIcon={<EmailIcon />}
								sx={{ mr: 1 }}
							>
								Request intro
							</Button>
							<IconButton aria-label="shortlist">
								<BookmarkIcon />
							</IconButton>
							<IconButton aria-label="share">
								<ShareIcon />
							</IconButton>
						</Box>
						<Typography variant="body2" color="text.secondary" sx={{ mt: 2 }}>
							{employeeDetailState?.summary}
						</Typography>
						<Typography variant="body2" color="text.primary" sx={{ mb: 1 }}>
							Expert in
						</Typography>
						<Box
							sx={{ mt: 2, display: "flex", justifyContent: "space-between" }}
						>
							<Box sx={{ display: "flex" }}>
								{employeeDetailState?.skillJSON?.map((skill) => (
									<Chip
										sx={{
											margin: "0 3px",
											backgroundColor: "#f4e9fe",
											color: "#b47ce7",
										}}
										label={skill.skillName}
									/>
								))}
							</Box>
							<Box sx={{ display: "flex" }}>
								<Typography variant="body2" color="primary">
									Hire instantly
								</Typography>
								<ArrowForwardOutlinedIcon />
							</Box>
						</Box>
						<Box
							sx={{
								mt: 3,
								display: "flex",
								justifyContent: "space-between",
								alignItems: "center",
								backgroundColor: "lightgrey",
							}}
						>
							<Grid container spacing={2}>
								{[
									"Interview",
									"Experience",
									"Education",
									"Awards",
									"Projects",
								].map((section, index) => (
									<Grid item key={section}>
										<Button
											variant="text"
											sx={{ color: "black" }}
											onClick={() => {
												if (section === "Interview")
													handleScrollTo(interviewRef);
												if (section === "Experience")
													handleScrollTo(experienceRef);
												if (section === "Education")
													handleScrollTo(educationRef);
												if (section === "Awards") handleScrollTo(awardsRef);
												if (section === "Projects") handleScrollTo(projectsRef); // Use this when the project section is added
											}}
										>
											{section}
										</Button>
									</Grid>
								))}
							</Grid>
						</Box>
						<Box sx={{ display: "flex", justifyContent: "center", padding: 2 }}>
							<Grid container spacing={3}>
								<Grid item>
									<Card>
										<CardContent>
											{employeeDetailState?.fullTime != null && (
												<div>
													<Typography variant="h6" component="div">
														Full-Time
													</Typography>
													<Typography
														variant="body2"
														color="text.secondary"
														sx={{ margin: "8px 0" }}
													>
														Can work 40+ hours / week immediately
													</Typography>
													<Typography variant="h6" component="div">
														{employeeDetailState?.fullTimeSalaryCurrency && "$"}
														{employeeDetailState?.fullTimeSalary} /month
													</Typography>
												</div>
											)}
										</CardContent>
									</Card>
								</Grid>
								<Grid item>
									<Card>
										<CardContent>
											{employeeDetailState?.partTime != null && (
												<div>
													<Typography variant="h6" component="div">
														Part-Time
													</Typography>
													<Typography
														variant="body2"
														color="text.secondary"
														sx={{ margin: "8px 0" }}
													>
														Can work 20+ hours / week immediately
													</Typography>
													<Typography variant="h6" component="div">
														{employeeDetailState?.partTimeSalaryCurrency && "$"}
														{employeeDetailState?.partTimeSalary} /month
													</Typography>
												</div>
											)}
										</CardContent>
									</Card>
								</Grid>
							</Grid>
						</Box>
						<Box
							sx={{
								width: "100%",
								maxWidth: 800,
								margin: "0 auto",
								padding: 2,
							}}
							ref={experienceRef}
						>
							<Typography variant="h6" gutterBottom>
								Work Experience
							</Typography>
							<Divider />
							{employeeDetailState?.workExperienceJSON?.map(
								(experience, index) => (
									<Box key={index} sx={{ display: "flex", mb: 4 }}>
										<Avatar
											src={
												"https://w7.pngwing.com/pngs/481/915/png-transparent-computer-icons-user-avatar-woman-avatar-computer-business-conversation-thumbnail.png"
											}
											alt={
												"https://w7.pngwing.com/pngs/481/915/png-transparent-computer-icons-user-avatar-woman-avatar-computer-business-conversation-thumbnail.png"
											}
											sx={{ width: 56, height: 56, mr: 2 }}
										/>
										<Box>
											<Typography variant="h6" component="div">
												{experience?.workExperienceRole}
											</Typography>
											<Typography variant="subtitle1" color="text.secondary">
												{experience?.workExperienceCompany}
											</Typography>
											<Typography variant="body2" color="text.secondary">
												{experience?.workExperienceDescription}
											</Typography>
											<Typography
												variant="body2"
												color="text.secondary"
												sx={{ mt: 1 }}
											>
												{experience?.workExperienceStartDate} -{" "}
												{experience?.workExperienceEndDate}
											</Typography>
										</Box>
									</Box>
								)
							)}
						</Box>
						<Box
							sx={{
								width: "100%",
								maxWidth: 800,
								margin: "0 auto",
								padding: 2,
							}}
							ref={educationRef}
						>
							<Typography variant="h6" gutterBottom>
								Education
							</Typography>
							<Divider />
							<List>
								{employeeDetailState?.educationJSON?.map((item, index) => (
									<ListItem
										key={index}
										sx={{
											display: "flex",
											justifyContent: "space-between",
											alignItems: "center",
										}}
									>
										<Box sx={{ display: "flex", alignItems: "center" }}>
											<ListItemAvatar>
												<Avatar alt={item.degree} src={item.icon}>
													{/* <SchoolIcon /> */}
												</Avatar>
											</ListItemAvatar>
											<ListItemText
												primary={
													<Typography>
														{item?.EducationDegree} ,{item?.EducationMajor}
													</Typography>
												}
												secondary={
													<Typography
														component="span"
														variant="body2"
														color="text.primary"
													>
														{item?.EducationSchool}
													</Typography>
												}
											/>
										</Box>
										<Typography
											variant="body2"
											color="textSecondary"
											sx={{ minWidth: "100px", textAlign: "right" }}
										>
											{item?.EducationStartDate} - {item?.EducationEndDate}
										</Typography>
									</ListItem>
								))}
							</List>
						</Box>
						<Box
							sx={{
								width: "100%",
								maxWidth: 800,
								margin: "0 auto",
								padding: 2,
							}}
							ref={awardsRef}
						>
							<Typography variant="h6" gutterBottom>
								Awards
							</Typography>
							<Divider />
							<Box component="ul" sx={{ paddingLeft: 2, marginTop: 1 }}>
								{awardsData?.map((award, index) => (
									<Typography
										component="li"
										variant="body2"
										key={index}
										sx={{ listStyleType: "disc", marginLeft: 2 }}
									>
										{award}
									</Typography>
								))}
							</Box>
						</Box>
						<Box
							sx={{
								width: "100%",
								maxWidth: 800,
								margin: "0 auto",
								padding: 2,
							}}
							ref={projectsRef}
						>
							<Typography variant="h6" gutterBottom>
								Projects
							</Typography>
							<Divider />
							{/* Add project details here */}
						</Box>
					</CardContent>
				</Card>
			</Box>
		</div>
	);
};

export default CardDetail;
