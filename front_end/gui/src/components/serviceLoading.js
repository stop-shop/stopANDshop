import React from 'react';
import '../css/style.css'

function ServiceLoading(Component) {
	return function ServiceLoadingComponent({ isLoading, ...props }) {
		if (!isLoading) return <Component {...props} />;
		return (
<section className="containerLoader">
  <h1>
    <span className="titleLoader">Stop </span>
    <span className="titleLoader">AND </span>
    <span className="titleLoader">Shop are loading ....</span>
  </h1>
  
</section>		);
	};
}
export default ServiceLoading;
