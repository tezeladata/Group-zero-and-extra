import React, { useContext, useEffect } from "react";
import useForm from "../Hooks/useForm.jsx";
import { StudentsContext } from "../Context/studentsContext";

const StudentForm = () => {
    const { info, handleChange, setInfo } = useForm();
    const { all, addStudent } = useContext(StudentsContext);

    const handleSubmit = (e) => {
        e.preventDefault();
        if (Object.keys(info).length > 0) {
            addStudent(info);
            setInfo({});
        }
    };

    useEffect(() => {
        console.log("Updated student list:", all);
    }, [all]);

    return (
        <section className="w-full h-screen flex items-center justify-center">
            <div className="flex items-center justify-center w-full h-screen bg-gradient-to-r from-stone-900 to-green-950 max-[700px]:flex-col">
                <div className="h-3/5 w-1/4 bg-gray-200 rounded-l-xl">
                    <h1 className="text-center pt-10 text-3xl font-MonaSpace font-bold cursor-pointer">Registration</h1>
                    <form className="w-full h-full flex flex-col items-center justify-center" onSubmit={handleSubmit}>
                        <input type="text" required placeholder="Username" name="username" onChange={handleChange} value={info.username || ""}
                            className="rounded-2xl text-center text-2xl text-white font-bold py-3 bg-green-900 border-0 mb-6" />
                        <input type="text" required placeholder="Facebook link" name="link" onChange={handleChange}
                               value={info.link || ""} className="rounded-2xl text-center text-2xl text-white font-bold py-3 bg-green-900 border-0 mb-6" />
                        <input type="email" required placeholder="Email" name="email" onChange={handleChange}
                               value={info.email || ""} className="rounded-2xl text-center text-2xl text-white font-bold py-3 bg-green-900 border-0 mb-6" />
                        <input type="password" required placeholder="Password" name="password" onChange={handleChange}
                               value={info.password || ""} className="rounded-2xl text-center text-2xl text-white font-bold py-3 bg-green-900 border-0 mb-6" />

                        <button type="submit" className="inline-block rounded bg-neutral-800 px-6 pb-2 pt-2.5 text-xl font-medium uppercase leading-normal text-neutral-50">
                            Submit
                        </button>
                        <br/>
                    </form>
                </div>

                <div className="w-1/4 h-3/5 bg-green-900 flex flex-col items-center justify-center rounded-r-xl">
                    <p className="p-6 text-2xl text-white"><span className="font-bold">Name:</span> {info.username}</p>
                    <p className="p-6 text-2xl text-white"><span className="font-bold">Facebook link:</span> {info.link}</p>
                    <p className="p-6 text-2xl text-white"><span className="font-bold">Email:</span> {info.email}</p>
                    <p className="p-6 text-2xl text-white"><span className="font-bold">Password:</span> {info.password}</p>
                </div>
            </div>
        </section>
    );
};

export default StudentForm;