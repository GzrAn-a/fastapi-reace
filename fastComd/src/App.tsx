import {useEffect, useState} from 'react'

import type {InHero} from "./interface/interfaceUser.ts";
import {ApigetUser} from "./apis/ApiGetUser.ts";


export function App() {
  const [users, setUsers] = useState<InHero[]>([])

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
      <>
        <h1 className="text-3xl font-bold underline">
          Hello world!
        </h1>
        <h1>Hero List</h1>
        {users.map((u) => (
            <div className="h-40 bg-pink-100" key={u.id}>
              <p className=" ">name: {u.name}</p>
              <p>age: {u.age}</p>
              <p>secret: {u.secret_name}</p>
            </div>
        ))}
      </>
  )
}



