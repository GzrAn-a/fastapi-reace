import {useEffect, useState} from "react";
import {getCode} from "../apis/ApiGetUser.ts";
import type {InImgCode} from "../interface/interfaceUser.ts";

export function PagesLogin() {
    const [from, setFrom] = useState({
        username: "",
        password: "",
    });
    const [code, setCode] = useState<InImgCode | null>(null);
    useEffect(() => {
        const fetchCode=
        async () => {
            const res = await getCode();
            setCode(res);
        }
        fetchCode();
    }, [])
    console.log("code",code)
    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setFrom({
            ...from,
            [e.target.name]: e.target.value,
        })
    }
    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        console.log("login", from)
    }
    const lang = {

        zh: {
            username: "账号",
            password: "密码",
            login: "登录"
        },
        en: {
            username: "Username",
            password: "Password",
            login: "Login"
        }
    }


    return (
        <div className="min-h-screen flex items-center justify-center  from-pink-200 via-purple-200 to-blue-200">

            <form onSubmit={handleSubmit}
                  className="w-80 p-6
                bg-white/10
                backdrop-blur-2xl
                border border-white/20

                shadow-[0_8px_32px_rgba(0,0,0,0.15)]

                rounded-3xl
                space-y-4 "
            >
                <h1 className="text-2xl font-bold text-center text-blue-400">
                    Login
                </h1>
                <input
                    name="username"
                    value={from.username}
                    onChange={handleChange}
                    placeholder={lang.en.username}
                    className="w-full p-2 rounded-lg bg-white/20 backdrop-blur border hover:scale-105 transition duration-300 border-white/30"/>
                <input
                    name="password"
                    value={from.password}
                    type="password"
                    onChange={handleChange}
                    placeholder={lang.en.password}
                    className={"w-full p-2 rounded-lg bg-white/20 hover:scale-105 transition duration-300 backdrop-blur border border-white/30"}
                />
                {code && <img src={code.img_url} />}
                <button
                    type="submit"
                    className={"w-full bg-pink-200 text-blue-500 hover:scale-105 transition duration-300 py-2 rounded-lg hover:bg-amber-200 transition"}>
                    {lang.en.login}</button>
            </form>
        </div>
    )
}