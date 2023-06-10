
"use strict";

const Nav = () => {
  return (
    <nav className="kgreen lighten-1" role="navigation">
      <div className="nav-wrapper container">
        <a id="logo-container" href="/" className="brand-logo">
          kitanda.shop
        </a>
      </div>
    </nav>
  );
};

customElements.define("nav-header", Nav);
