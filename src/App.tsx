import React, { useState } from 'react';
import './App.css';

interface InputItem {
  id: number;
  value: string;
}

const App: React.FC = () => {
  const [inputs, setInputs] = useState<InputItem[]>([
    { id: 1, value: 'Input 1' },
    { id: 2, value: 'Input 2' },
    { id: 3, value: 'Input 3' },
    { id: 4, value: 'Input 4' },
    { id: 5, value: 'Input 5' },
  ]);

  const [newInputValue, setNewInputValue] = useState<string>('');

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setNewInputValue(e.target.value);
  };

  const handleAddInput = () => {
    if (newInputValue.trim() === '') {
      alert('Por favor, insira um valor para adicionar.');
      return;
    }

    const newInput: InputItem = {
      id: Date.now(), // Usando timestamp como ID para garantir único
      value: newInputValue,
    };

    setInputs([...inputs, newInput]);
    setNewInputValue(''); // Limpar o campo de entrada após adicionar
  };

  const handleDragStart = (e: React.DragEvent<HTMLDivElement>, index: number) => {
    e.dataTransfer.setData('index', index.toString());
    // Adicionar classe CSS para indicar que está arrastando
    e.currentTarget.classList.add('dragging');
  };

  const handleDragOver = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    e.dataTransfer.dropEffect = 'move'; // Define o efeito de drop como 'move'
  };

  const handleDrop = (e: React.DragEvent<HTMLDivElement>, targetIndex: number) => {
    const dragIndex = parseInt(e.dataTransfer.getData('index'), 10);
    const dragInput = inputs[dragIndex];

    // Remove o input da lista original
    const updatedInputs = inputs.filter((_, index) => index !== dragIndex);

    // Insere o input na nova posição
    updatedInputs.splice(targetIndex, 0, dragInput);

    setInputs(updatedInputs);

    // Remover classe CSS de arrastando ao soltar
    const draggedElement = document.querySelector('.dragging');
    if (draggedElement) {
      draggedElement.classList.remove('dragging');
    }
  };

  return (
    <div className="app">
      <h1>Arraste e Solte Inputs</h1>
      <div className="input-list">
        {inputs.map((input, index) => (
          <div
            key={input.id}
            className="input-item"
            draggable
            onDragStart={(e) => handleDragStart(e, index)}
            onDragOver={(e) => handleDragOver(e)}
            onDrop={(e) => handleDrop(e, index)}
          >
            {input.value}
          </div>
        ))}
      </div>
      <div className="add-input">
        <input
          type="text"
          value={newInputValue}
          onChange={handleInputChange}
          placeholder="Novo Input"
        />
        <button onClick={handleAddInput}>Adicionar</button>
      </div>
    </div>
  );
};

export default App;
