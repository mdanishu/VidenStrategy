import React from 'react';

const Contact: React.FC = () => {
return (
	<div>
	<h2>Email me at Danish@videnstrategy.com</h2>
	<iframe 
        width="640px" 
        height="480px" 
        src="https://forms.office.com/r/DBdrmtmaHM?embed=true" 
        frameBorder={0}
        marginWidth={0} 
        marginHeight={0} 
        style={{border: 'none', maxWidth: '100%', maxHeight: '100vh'}} 
        allowFullScreen 
        // webKitAllowFullScreen 
        // mozAllowFullScreen 
        // msAllowFullscreen
        >
      </iframe>
	</div>

	
);
};

export default Contact;
