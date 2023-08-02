import React from "react";
import styled from "styled-components";

export const MenuItem = React.forwardRef((props, ref) => {
  const { active, disabled, children, ...rest } = props;

  return (
    <Root {...rest} ref={ref} disabled={disabled} active={active}>
      {children}
    </Root>
  );
});

const Root = styled.div`
  width: 118px;
  min-height: auto;
  padding: 5px 10px;
  border: none;
  cursor: ${(p) => (p.disabled ? "initial" : "pointer")};
  opacity: ${(p) => (p.disabled ? 0.5 : 1)};
  background-color: ${(p) => (p.active ? "#ccc" : "#fff")};
`;