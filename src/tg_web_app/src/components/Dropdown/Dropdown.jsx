import React from "react";
import styled from "styled-components";

export const Dropdown = ({ label, children, onChange, isEnable, value }) => {
  const [isOpen, setOpen] = React.useState(false);
  const [selected, setSelected] = React.useState(null);
  const [highlightedIndex, setHighlightedIndex] = React.useState(-1);
  const dropdownRef = React.useRef(null);

  const handleOpen = () => setOpen(!isOpen);
  const handleClose = () => setOpen(false);

  React.useEffect(() => {
    if (selected) {
      onChange(selected);
      handleClose();
    }
  }, [selected]);

  React.useEffect(() => {
    if (value) {
      setSelected(value);
    }
  });

  const handleChange = (item) => {
    onChange(item);
    setSelected(item);
  };

  React.useEffect(() => {
    const handleOutsideClick = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        handleClose();
      }
    };

    document.addEventListener("mousedown", handleOutsideClick);

    return () => {
      document.removeEventListener("mousedown", handleOutsideClick);
    };
  }, []);

  return (
    <Root ref={dropdownRef}>
      <Control onClick={handleOpen} type="button">
        <svg
          width="12"
          height="6"
          viewBox="0 0 12 6"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          style={{
            paddingRight: ".3rem",
          }}
        >
          <path
            d="M11 1L6 5L1 1"
            stroke={isEnable ? "white" : "black"}
            strokeWidth="1.5"
            strokeLinecap="round"
            strokeLinejoin="round"
          />
        </svg>
        {selected ? selected.name : label}
      </Control>
      {isOpen && isEnable && (
        <Menu>
          {React.Children.map(children, (child, index) => {
            if (React.isValidElement(child)) {
              return React.cloneElement(child, {
                active: index === highlightedIndex,
                onMouseEnter: () => setHighlightedIndex(index),
                onClick: () => handleChange(child.props.value),
              });
            }
          })}
        </Menu>
      )}
    </Root>
  );
};

const Root = styled.div`
  width: 30%;
  margin-bottom: 0.3rem;
`;

const Control = styled.button`
  width: 100%;
  margin: 0;
  padding: 0.5rem;
  border: none;
  border-radius: 0.25rem;
  background-color: #50a7ea;
  color: white;
  text-align: left;
`;

const Menu = styled.menu`
  position: absolute;
  margin: 0;
  padding: 0;
  margin-top: 1px;
  border: 1px solid grey;
  max-height: 100px;
  overflow-y: auto;
  z-index: 100;
`;
