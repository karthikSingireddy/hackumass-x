import React from 'react'

function DiningHall(props) {
    return (
        <div className='diningHall' onClick={() => {console.log(props.name)}}>
            <img src={require("./" + props.name + ".jpg")} alt="image not found"/>
        </div>
    );
}

export default DiningHall;