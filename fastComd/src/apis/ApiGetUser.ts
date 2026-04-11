import axios from "axios"
import type {InHero, InGetHero} from "../interface/interfaceUser.ts";

const BaseUrl:string = "http://127.0.0.1:8000"
export async function ApigetUser(params?: InGetHero): Promise<InHero[]> {
    const res = await axios.get(`${BaseUrl}/api_v1/heroes/`, {
        params: params
    })

    return res.data
}