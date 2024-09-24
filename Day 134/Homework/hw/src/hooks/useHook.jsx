import { useState} from "react";

const useHook = () => {
    const [info, setInfo] = useState({});

    const handleChange = (e) => {
        const { name, value } = e.target;
        setInfo(prev => ({
            ...prev,
            [name]: value
        }))
    }

    return {info, handleChange};
}

export default useHook;