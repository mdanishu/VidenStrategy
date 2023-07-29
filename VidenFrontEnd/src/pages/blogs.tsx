import React from 'react';

const Blogs: React.FC = () => {
  const openSubstack = () => {
    window.open('https://viden.substack.com/', '_blank');
  };

  const openX = () => {
    window.open('https://twitter.com/VidenDanish/', '_blank');
  };

  return (
	<div className="Blogs">
	<h2>
            Substack and X are where I will post my analysis and opinions.
          </h2>
          <button className="nav-button blogs-button" onClick={openSubstack}>
        Go to Substack
      </button>
      <button className="nav-button blogs-button" onClick={openX}>
        Go to X
      </button>
        
</div>);
};

export default Blogs;
