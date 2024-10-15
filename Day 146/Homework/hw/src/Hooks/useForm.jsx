import { useState } from "react";

const useForm = () => {
    const [info, setInfo] = useState({});

    const handleChange = (e) => {
        const { name, value } = e.target;
        setInfo(prev => ({
            ...prev,
            [name]: value
        }));
    };

    return { info, handleChange, setInfo };
};

export default useForm;