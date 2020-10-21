// import React from 'react';
import './App.css';
// import Login from './components/login';
import React, { useEffect, useState } from 'react';
import './App.css';
import Services from './components/service';
import ServiceLoadingComponent from './components/serviceLoading';

function App() {
	const ServiceLoading = ServiceLoadingComponent(Services);
	const [appState, setAppState] = useState({
		loading: false,
		services: null,
	});

	useEffect(() => {
		setAppState({ loading: true });
		const apiUrl = `https://stopandshopapp.herokuapp.com/api/shop/`;
    fetch(apiUrl)
    // console.log(apiUrl)

			.then((data) => data.json())
			.then((services) => {
        setAppState({ loading: false, services: services });
			});
	}, [setAppState]);
	return (
		<div className="App">
			<h1>Latest services</h1>
			<ServiceLoading isLoading={appState.loading} services={appState.services} />
		</div>
	);
}
export default App;
