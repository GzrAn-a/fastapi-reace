import {useEffect, useState} from 'react'

import type {InHero} from "./interface/interfaceUser.ts";
import {ApigetUser} from "./apis/ApiGetUser.ts";
import {useNavigate} from "react-router-dom";


export function App() {
    const [users, setUsers] = useState<InHero[]>([])
    const navigate = useNavigate()
    useEffect(() => {
        const fetchData = async () => {
            const data = await ApigetUser({
                offset: 0,
                limit: 10
            })
            console.log(data)
            setUsers(data)
        }

        fetchData()
    }, [])

    return (


        <div className="flex flex-col items-center justify-center ">

            <h1 className="text-6xl">Hello world!</h1>

            {users.map((u: InHero)=> (

                <div key={u.id}
                     onClick={() => navigate(`/hero/${u.id}`)}
                     className="w-50 rounded-2xl border  border-white/30 bg-white/20 backdrop-blur-md shadow-lg  flex flex-wrap gap-4 justify-center p-6 ">
                    <p>name: {u.name} </p>
                    <p>age: {u.age}</p>
                    <p>secret: {u.secret_name}</p>

                </div>
            ))}
        </div>

    )
}


