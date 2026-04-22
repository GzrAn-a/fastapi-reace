import './index.css'
import ReactDOM from 'react-dom/client'

import {BrowserRouter, Routes, Route} from "react-router-dom"
import {HeroSelf} from "./pages/Hreo.tsx";
import {PagesLogin} from "./pages/PagesLogin.tsx";

ReactDOM.createRoot(document.getElementById('root')!).render(
    <BrowserRouter>
        <Routes>
            {/*<Route path="/" element={<App/>}/>*/}
            <Route path="/" element={ <PagesLogin/>}/>
            <Route path="/hero/:id" element={<HeroSelf/>}/>

        </Routes>
    </BrowserRouter>
)