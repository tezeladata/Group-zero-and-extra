import { useEffect, useState } from "react";

export const usePosition = () => {
    const [position, setPosition] = useState(() => {
        return Number(localStorage.getItem("Position")) || 0;
    });

    const updatePosition = () => {
        const scrollPosition = window.scrollY;
        setPosition(scrollPosition);
        localStorage.setItem("Position", scrollPosition);
    };

    useEffect(() => {
        window.addEventListener("scroll", updatePosition);

        const savedPosition = Number(localStorage.getItem("Position")) || 0;
        window.scrollTo(0, savedPosition);

        return () => {
            window.removeEventListener("scroll", updatePosition);
        };
    }, []);

    return { position };
};