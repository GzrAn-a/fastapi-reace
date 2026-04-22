import {useParams} from "react-router-dom";

export function HeroSelf() {
    const {id} = useParams()
    return (
        <div>
            <h1>Hero Detail</h1>
            <p>Hero ID: {id}</p>
        </div>
    )
}