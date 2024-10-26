import React, {memo} from 'react';

const MemoizedInput = memo(({ value, onChange, placeholder, type }) => {
  console.log(`Rendering input: ${placeholder}`);

  return (
    <input
      type={type}
      value={value}
      onChange={onChange}
      placeholder={placeholder}
      style={{ marginBottom: '10px', padding: '8px', width: '200px' }}
    />
  );
});

export default MemoizedInput;